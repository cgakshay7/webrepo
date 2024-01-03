class Rectangle:
	def__init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	
	def area(self):
		return self.length*self.breadth
	
	def perimeter(self):
		return 2*(self.length+self.breadth)
		
	def compare_area(self,other_rectangle):
		if self.area()>other_rectangle.area():
			return "the first rectangle has larger area."
			
		elif self.area()<other_rectangle.area():
			return"the second rectangle has a larger area"
		else:
			return"both rectangles have same area"
			
rectangle1=Rectangle(5,8)
rectangle2=Rectangle(4,10)

print("area of rectangle 1",rectangle1.area())
print("perimeter of rectangle 1",rectangle1.perimeter())

print("area of rectangle 2",rectangle2.area())
print("perimeter of rectangle 2",rectangle2.perimeter())

comparison_result=rectangle1.compare_area(rectangle2)
print(comparison_result)

			
