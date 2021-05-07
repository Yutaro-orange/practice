import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn.model_selection import KFold
import xgboost as xgb

train_data_csv = pd.read_csv('C:/users/taro_/Desktop/conpetition_data/cellphone/train.csv')
test_data_csv = pd.read_csv('C:/users/taro_/Desktop/conpetition_data/cellphone/test.csv')


train_data = pd.DataFrame(train_data_csv)
test_data = pd.DataFrame(test_data_csv)

X_train = train_data[['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc',
       'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc',
       'px_height', 'px_width', 'ram', 'talk_time', 'three_g',
       'touch_screen', 'wifi']]
y_train = train_data[['price_range']]

test_x = test_data[['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc',
       'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc',
       'px_height', 'px_width', 'ram', 'talk_time', 'three_g',
       'touch_screen', 'wifi']]






##X_train = pd.concat([X_train[['three_g','n_cores','touch_screen', 'wifi']],X_mobile_dummies
##,X_battery_dummies,X_clock_dummies,X_ram_dummies,X_talk_dummies,X_sc_h_dummies,X_fc_dummies], axis=1)



#テスト用データの整形
##test_x_mobile_cut, bin_mobile_indice = pd.cut(test_x["mobile_wt"], bins=bins_mobile, retbins=True, labels=False)
##test_x_battery_cut, bin_battery_indice = pd.cut(test_x["battery_power"], bins=bins_battery, retbins=True, labels=False)
##test_x_clock_cut, bin_clock_indice = pd.cut(test_x["clock_speed"], bins=bins_clock, retbins=True, labels=False)
##test_x_ram_cut, bin_ram_indice = pd.cut(test_x["ram"], bins=bins_ram, retbins=True, labels=False)
##test_x_talk_cut, bin_ram_indice = pd.cut(test_x["talk_time"], bins=bins_talk, retbins=True, labels=False)
##test_x_px_height_cut, bin_px_height_indice = pd.cut(test_x["px_height"], bins=bins_px_height, retbins=True, labels=False)
##test_x_sc_h_cut, bin_sc_h_indice = pd.cut(test_x["sc_h"], bins=bins_sc_h, retbins=True, labels=False)
##test_x_core_cut, bin_core_indice = pd.cut(test_x["n_cores"], bins=bins_core, retbins=True, labels=False)
##test_x_fc_cut, bin_fc_indice = pd.cut(test_x["fc"], bins=bins_fc, retbins=True, labels=False)
##test_x_m_dep_cut,bin_x_m_dep_cut = pd.cut(test_x["m_dep"], bins=bins_m_dep, retbins=True, labels=False)
##
##test_x_mobile_dummies = pd.get_dummies(test_x_mobile_cut, prefix=test_x_mobile_cut.name)
##test_x_battery_dummies = pd.get_dummies(test_x_battery_cut, prefix=test_x_battery_cut.name)
##test_x_clock_dummies = pd.get_dummies(test_x_clock_cut, prefix=test_x_clock_cut.name)
##test_x_ram_dummies = pd.get_dummies(test_x_ram_cut, prefix=test_x_ram_cut.name)
##test_x_talk_dummies = pd.get_dummies(test_x_talk_cut, prefix=test_x_talk_cut.name)
##test_x_px_height_dummies = pd.get_dummies(test_x_px_height_cut, prefix=test_x_px_height_cut.name)
##test_x_sc_h_dummies = pd.get_dummies(test_x_sc_h_cut, prefix=test_x_sc_h_cut.name)
##test_x_core_dummies = pd.get_dummies(test_x_core_cut, prefix=test_x_core_cut.name)
##test_x_fc_dummies = pd.get_dummies(test_x_fc_cut, prefix=test_x_fc_cut.name)
##test_x_m_dep_dummies = pd.get_dummies(test_x_m_dep_cut, prefix=test_x_m_dep_cut.name)

##X_train = pd.concat([X_train[['four_g','n_cores','touch_screen', 'wifi']],X_m_dep_dummies,X_clock_dummies,X_battery_dummies,
##X_ram_dummies,X_talk_dummies,X_fc_dummies], axis=1)
##
##
##test_x = pd.concat([test_x[['four_g','n_cores','touch_screen', 'wifi']],test_x_m_dep_dummies
##        ,test_x_clock_dummies,test_x_battery_dummies,test_x_ram_dummies,test_x_talk_dummies,
##        test_x_fc_dummies], axis=1)




#学習データを4つに分割し、うち一つをバリデーションデータとする
##kf = KFold(n_splits=4,shuffle=True,random_state=71)
##tr_idx,va_idx=list(kf.split(X_train))[0]
##
###学習データを学習データとバリデーションデータに分ける
##tr_x,va_x = X_train.iloc[tr_idx],X_train.iloc[va_idx]
##tr_y,va_y = y_train.iloc[tr_idx],y_train.iloc[va_idx]

#特徴量と目的変数をxgboostのデータ構造へと変換
##dtrain = xgb.DMatrix(tr_x,label=tr_y)
##dvaliid = xgb.DMatrix(va_x,label=va_y)
##dtest = xgb.DMatrix(test_x)
##
###ハイパーパラメータの設定
##params = {'objrextive':'binary:logistic','silent':1,'random_state':71}
##num_round=50
##
###学習実行
##watchlist = [(dtrain,'train'),(dvaliid,'eval')]
##model = xgb.train(params,dtrain,num_round,evals=watchlist)
##
###バリデーションデータでのスコアの確認
##va_pred = model.predict(dvaliid)
##score = log_loss(va_y,va_pred)
##print(f'logloss:{score:4f}')
##pred = model.predict(dtest)


#今回はランダムフォレストでモデリングを行うこと
clf = RandomForestClassifier(random_state=1)
clf.fit(X_train,y_train)
y_pred = clf.predict(test_x)
print(y_pred)

id = np.array(test_data["id"]).astype(int)

answer = pd.DataFrame(y_pred,id , columns = ["rank"])

answer.to_csv("C:/users/taro_/Desktop/conpetition_data/cellphone/price_predict.csv",index_label = ["rank"],header=False)

