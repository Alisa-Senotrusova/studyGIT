fun main() {

    val f = Rect(0,3,1,2)

    println("Rotation Rect(" + f.c_pos() +") around (x:0,y:0) Clockwise: ")
    f.rotate(RotateDirection.Clockwise,0,0)
    println(f.c_pos())

    println("Resize x2, Rect S = " + f.area())
    f.resize(2)
    println(f.area())

    val f1 = Square(7,7,2)

    println("Rotation Square(" + f1.c_pos() + ") around (x:7,y:4) Clockwise: ")
    f1.rotate(RotateDirection.CounterClockwise,7,4)
    println(f1.c_pos())

    println("Resize x2, Square S = " + f1.area())
    f1.resize(2)
    println(f1.area())

    val f2 = Circle(2,2,3)

    println("Rotation Circle(" + f2.c_pos() + ") around (x:0,y:0) Clockwise: ")
    f2.rotate(RotateDirection.Clockwise,0,0)
    println(f2.c_pos())

    println("Resize x2,  Circle S= " + f2.area())
    f2.resize(2)
    println(f2.area())
}