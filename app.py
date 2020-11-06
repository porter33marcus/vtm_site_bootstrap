from flask import Flask
from flask import render_template, request

app = Flask(__name__)

class Tank:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.materialCost = 0.0
        self.laborCost = 0.0
        self.totalCost = 0.0
        self.pi = 3.14
        self.top = 0.0
        self.sides = 0.0
        self.totalArea = 0.0
    def calculateAreaTop(self):
        self.top = self.pi*(self.radius**2)
    def calculateAreaSides(self):
        self.Sides = 2*(self.pi*(self.radius*self.height))
    def calculateTotalArea(self):
        self.calculateAreaTop()
        self.calculateAreaSides()
        self.totalArea= self.top + self.sides
    def calculateMaterialCost(self):
        self.calculateTotalArea()
        self.materialCost = self.totalArea*25.00
    def calculateLaborCost(self):
        self.calculateTotalArea()
        self.laborCost = self.totalArea*15.00
    def calculateTotalCost(self):
        self.calculateLaborCost()
        self.calculateMaterialCost()
        self.totalCost = self.laborCost + self.materialCost
    def getTotalCost(self):
        return self.totalCost
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')
@app.route('/tankCalc', methods=['POST'])
def tankCalc():
    if request.method == 'POST':
        form = request.form
        height = float(form['height'])
        radius = float(form['radius'])
        
        tank = Tank(height, radius)
        tank.calculateTotalCost()
        tankCost = tank.getTotalCost()
        
        return render_template('estimate.html', tankCalc = tankCost)
    return render_template('estimate')

if __name__ == '__main__':
    app.run(debug=True)