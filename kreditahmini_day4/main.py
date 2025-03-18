import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np


#eğitim ve test verilerini yükleme
train_data=pd.read_csv("day4/data/train_kredi_tahmini.csv") #eğitim verisi
test_data=pd.read_csv("day4/data/test_kredi_tahmini.csv") #test verisi
#############################################
#orijinal veri kopyasını oluşturma
train_original=train_data.copy()
test_original=test_data.copy() #kopyasını yaptık böylece bir değişiklik olsa da orjinal veri setini kaybetmeyiz

#veri setinin ilk 5 satırını görüntüleme
print("Eğitim verisi:")
print(train_data.head()) #method

print("\neğitim verisi column:")
print(train_data.columns) #attribute

print("\nTest verisi:")
print(test_data.head())
################################################
#tüm boş NaN hücreleri en sık kullanılan degerle doldurma

for column in train_data.columns:
    most_common_value = train_data[column].mode()[0]#en sık kullanılan degeri aldık
    train_data[column].fillna(most_common_value,inplace=True)

for column in test_data.columns:
    most_common_value=test_data[column].mode()[0]
    test_data[column].fillna(most_common_value,inplace=True)

print("\nEksik degerler dolduruldu!")

#Loan_ID çıkartıldı
train_data.drop(columns=["Loan_ID"], inplace=True)
test_data.drop(columns=["Loan_ID"],inplace=True)

#Dependents sütununu sayısala çevirdik
train_data["Dependents"]=train_data["Dependents"].replace("3+",4).astype(float)
test_data["Dependents"]=test_data["Dependents"].replace("3+",4).astype(float)

#Loan_Status sayısala çevir
train_data.replace({"Loan_Status":{'Y': 1, 'N': 0}
},inplace=True)

train_data.replace({
    'Married':{'No':0,'Yes':1},
    'Gender':{'Male':1,'Female':0},
    'Education':{'Graduate':1,'Not Graduate':0},
    'Self_Employed':{'Yes':1,'No':0},
    'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2}
},inplace=True)

test_data.replace({
    'Married':{'No':0,'Yes':1},
    'Gender':{'Male':1,'Female':0},
    'Education':{'Graduate':1,'Not Graduate':0},
    'Self_Employed':{'Yes':1,'No':0},
    'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2}
},inplace=True)

print("\nKategorik verilerin dönüştürülmesi sonrası eğitim verisi:")
print(train_data.head())

print("\nKategorik verilerin dönüştürülmesi sonrası test verisi:")
print(test_data.head())

train_data["Credit_History"] = train_data["Credit_History"].astype(float)
test_data["Credit_History"] = train_data["Credit_History"].astype(float)

print("\nTrain Data Sütunları:")
print(train_data.columns)

X = train_data.drop(columns=["Loan_Status"])
y = train_data["Loan_Status"]

print("\nVeri seti başarıyla hazırlandı!")

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)
print("\nEğitim ve test setleri başarıyla oluşturuldu!")

print(train_data["Dependents"].unique())
#####################################################
#veriyi ölçeklendirme
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
print("\nVeri ölçeklendirildi!")

#modeli eğitme
model=LogisticRegression()
model.fit(X_train,y_train)
print("\nModel eğitildi!")

#modelin doğruluğuna baktık
accuracy = model.score(X_test, y_test)
print(f"\nTest seti doğruluk oranı: {accuracy:.2f}")

#test verisi için tahmin ve sonucu kaydediyoruz
test_data_scaled=scaler.transform(test_data)
predictions=model.predict(test_data_scaled)

output=pd.DataFrame({"Tahmin":predictions})
output.to_csv("day4/data/kredi_tahmin_sonucu.csv",index=False)
print("\n Tahminler kaydedildi")

#################################################
#kullanıcımızı biz belirliyoruz ve tahmin ediyoruz kredi alabilir mi alamaz mı

#bu müşteri kredi alamaz
new_customer=pd.DataFrame({
    "Gender":[1], #male
    "Married":[1], #yes
    "Dependents":[0],
    "Education":[0], #graduate
    "Self_Employed":[0], #yes
    "ApplicantIncome":[500], #revenue
    "CoapplicantIncome":[500], #join revenue
    "LoanAmount":[150], #credit amount
    "Loan_Amount_Term":[360], #month
    "Credit_History":[0], #good
    "Property_Area":[2] #urban    
})

new_customer_scaled=scaler.transform(new_customer)

prediction=model.predict(new_customer_scaled)

if prediction[0]==1:
    print("\nBu müşteri kredi alabilir")
else:
    print("\nBu müşteri kredi alamaz")
