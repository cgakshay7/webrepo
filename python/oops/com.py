class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
	
	def perimeter(self):
		return 2*(self.length+self.breadth)
		
	def compare(self,other_rectangle):
		if self.area()>other_rectangle.area():
			print("rectangle 1 has larger area");
		elif self.area()<other_rectangle.area():
			print("rectangle 2 has larger area");
		else:
			print("invalid result or both rectangle has same area");
		
		
	
print("rectangle 1 is");
length=int(input("enter the length"));
breadth=int(input("enter the breadth"));
s1=Rectangle(length,breadth)
print("area is",s1.area())
print("perimeter",s1.perimeter())
print("rectangle 2 is");
length=int(input("enter the length"));
breadth=int(input("enter the breadth"));
s2=Rectangle(length,breadth)
print("area is",s2.area())
print("perimeter",s2.perimeter())
print("******compare******");
comparison_result = s1.compare(s2)
print(comparison_result);

