import java.math.RoundingMode
import kotlin.math.sqrt

data class CiResult(val min: Double, val max: Double)

class ConfidenceInterval {

    fun interval(index: Double, std: Double, rootN: Double): Double {
        return index * std / rootN
    }

    fun ci95(samples: IntArray): CiResult {
        // mean, std, n
        val n = samples.size
        val mean = samples.average()
        val meanSquare = mean * mean // E(X) ^ 2
        val meanXSquare = samples.sumOf { it * it } / n // E(X^2)
        val std = sqrt(meanXSquare - meanSquare)

        val intervalValue = interval(1.96, std, sqrt(n.toDouble()))
        val ci_min = mean - intervalValue
        val ci_max = mean + intervalValue

        return CiResult(ci_min, ci_max)
    }

    fun ci95_round(samples: IntArray, round: Int): CiResult {
        val result = ci95(samples)
        val ciMin = result.min.toBigDecimal().setScale(round, RoundingMode.HALF_UP).toDouble()
        val ciMax = result.max.toBigDecimal().setScale(round, RoundingMode.HALF_UP).toDouble()

        return CiResult(ciMin, ciMax)
    }
}