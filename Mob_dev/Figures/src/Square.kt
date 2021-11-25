import kotlin.math.cos
import kotlin.math.sin
// TODO: дополнить определение класса размерами и позицией
class Square(var x: Int, var y: Int, var h_w: Int) : Movable, Transforming, Figure(1) {
    // TODO: унаследовать от Figure, реализовать area()
    // TODO: реализовать интерфейс Transforming
    var color: Int = -1

    lateinit var name: String
    constructor(square: Square) : this(square.x, square.y, square.h_w)

    override fun move(dx: Int, dy: Int) {
        x += dx; y += dy
    }

    override fun resize(zoom: Int){
        h_w*=zoom
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

    override fun c_pos():String {
        return(("x:$x y:$y").toString())
    }

    override fun area(): Float {
        return  (h_w*h_w).toFloat()
    }
}