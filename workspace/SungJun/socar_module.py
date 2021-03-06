import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler
from sklearn.decomposition import PCA
from imblearn.over_sampling import SMOTE, ADASYN, SVMSMOTE, RandomOverSampler, BorderlineSMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTETomek, SMOTEENN
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score


class SocarML:

    def __init__(self, data, random_state=13, drop_cols=[]):
        self.data = data
        self.num_attribs = ['accident_ratio', 'repair_cost', 'insure_cost', 'repair_cnt']
        self.random_state=random_state
        self.drop_cols = drop_cols
        # classifier
        self.lg_clf = LogisticRegression(random_state=self.random_state)
        self.dt_clf = DecisionTreeClassifier(random_state=self.random_state, max_depth=2)
        self.rf_clf = RandomForestClassifier(random_state=self.random_state, n_jobs=-1, n_estimators=100)
        self.lgbm_clf = LGBMClassifier(random_state=self.random_state, n_estimators=200, num_leaves=16, n_jobs=-1, boost_from_average=False)
        self.svm_clf = LinearSVC(random_state=self.random_state)
        # hyper-parameters
        self.lg_params=[{'C':[0.1, 0.5, 1]}]
        self.dt_params= [{'max_depth': [2, 4, 6, 8]}]
        self.rf_params = [{'n_estimators': [50, 100, 200, 400]}]
        self.lgbm_params = [{'n_estimators': [50, 100, 200, 400], 'num_leaves': [4, 8, 16, 32]}]
        self.svm_params = [{'C':[0.1, 0.5, 1]}]

    def drop_columns(self, drop_cols):
        self.drop_cols = drop_cols
        self.data = self.data.drop(self.drop_cols, axis=1)

    def one_hot_encoding(self):
        cat_attribs = self.data.columns.drop(['fraud_YN', 'test_set'] + [attrib for attrib in self.num_attribs if attrib not in self.drop_cols])
        self.data = pd.get_dummies(self.data, columns=cat_attribs)

    def split_dataset(self):
        self.train_data = self.data[self.data.test_set == 0].drop(['test_set'], axis=1)
        self.test_data = self.data[self.data.test_set == 1].drop(['test_set'], axis=1)
        
        self.X = self.train_data.drop('fraud_YN', axis=1)
        self.y = self.train_data.fraud_YN
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(
            self.X, self.y, test_size=0.2, random_state=self.random_state, stratify=self.y)

        self.X_test = self.test_data.drop('fraud_YN', axis=1)
        self.y_test = self.test_data.fraud_YN

    def scaling(self, scaler):
        self.num_attribs = [attrib for attrib in self.num_attribs if attrib not in self.drop_cols]
        scaler_obj = scaler()
        scaler_obj.fit(self.X_train[self.num_attribs])

        for dataset in [self.X_train, self.X_val, self.X_test]:
            dataset[self.num_attribs] = scaler_obj.transform(dataset[self.num_attribs])

    def sampling(self, sampler):
        spl = sampler(random_state=self.random_state)
        self.X_train, self.y_train = spl.fit_sample(self.X_train, self.y_train)  

    def pca(self, n_components):       
        self.X_train, pca_n = self.get_pca_data(self.X_train, n_components)
        self.X_val, pca_n = self.get_pca_data(self.X_val, n_components)
        self.X_test, pca_n = self.get_pca_data(self.X_test, n_components)

    def get_pca_data(self, data, n_components):
        pca = PCA(n_components=n_components, random_state=self.random_state)
        pca.fit(data)

        return pca.transform(data), pca
    
    def get_result_pd(self):
        self.models = [(self.lg_clf,self.lg_params), (self.dt_clf,self.dt_params), (self.rf_clf,self.rf_params), 
                (self.lgbm_clf,self.lgbm_params), (self.svm_clf,self.svm_params)]
        self.model_names = ['LogisticRegression','DecisionTree','RandomForest','LightGBM', 'SVM']
        col_names = ['accuracy','precision','recall', 'test_accuracy','test_precision','test_recall']
        tmp = []
        
        for model, param in self.models:
            # Modeling    
            kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=self.random_state)
            grid = GridSearchCV(model, param, cv=kfold, scoring = 'recall')
            grid.fit(self.X_train, self.y_train)
            print(grid.best_params_)

            # predict validation dataset
            pred_val = grid.predict(self.X_val)
            
            # predict test dataset
            pred_test = grid.predict(self.X_test)
            
            tmp.append(self.get_clf_eval(self.y_val, pred_val) + self.get_clf_eval(self.y_test, pred_test))
            
        df = pd.DataFrame(tmp, columns=col_names, index=self.model_names)
        df = df.style.applymap(self.color)
            
        return df

    def get_clf_eval(self, y_test, pred):
        acc = accuracy_score(y_test, pred)
        pre = precision_score(y_test, pred)
        re = recall_score(y_test, pred)

        return acc, pre, re

    def color(self, val):
        color = 'orange' if val > 0.6 else 'black'
        return 'color: %s' % color

