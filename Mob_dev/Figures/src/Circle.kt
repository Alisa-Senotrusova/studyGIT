import kotlin.math.cos
import kotlin.math.sin
// TODO: дополнить определение класса размерами и позицией
class Circle(var x: Int, var y: Int, var r: Int) : Movable, Transforming, Figure(2) {
    // TODO: реализовать интерфейс Transforming
    var color: Int = -1
    val pi: Double = 3.14

    lateinit var name: String
    constructor(circle: Circle) : this(circle.x, circle.y, circle.r)

    override fun resize(zoom: Int){
        r*=zoom
    }

    override fun rotate(direction: RotateDirection, centerX: Int, centerY: Int){


        when(direction){
            RotateDirection.Clockwise -> {
                x = y - centerY + centerX.also { y = -1 * (x - centerX) + centerY }
            }
            RotateDirection.CounterClockwise -> {
                x = -1 * (y - centerY) + centerX.also { y = x - centerX + centerY }
            }
        }
    }
    override fun move(dx: Int, dy: Int) {
        x += dx; y += dy
    }
    override fun c_pos():String {
        return(("x:$x y:$y").toString())
    }

    override fun area(): Float {
        return  (pi*r*r).toFloat()
    }
}