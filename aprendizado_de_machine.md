
# REGRESSAO LINEAR
import statsmodels.api as sm

Y = values
X = features
X = sm.add_constant(X)
model = sm.OLS(Y, X)
results = model.fit()
   
intercept = results.params[0]
params = results.params[1:]

params[0] * x1 + params[1] * x2 + intercept

a1 * x1 + a2 * x2 + intercept

# COEFICIENTE DE DETERMINAÇÃO
Quanto mais proximo de 1, melhor é o modelo

data = y1, y2, ... yn
predictions = f1, f2, ... fn
media de data = media de y

1 - somatorio (yi - fi) ao quadrado dividido por somatorio (yi - media de y) ao quadrado

SSReg = (data - predictions) ** 2
SST = (data - np.mean(data)) ** 2
r_squared = 1 - ( np.sum(SSReg) / np.sum(SST) )


