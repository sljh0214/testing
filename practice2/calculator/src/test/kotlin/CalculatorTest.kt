import io.mockk.every
import io.mockk.mockk
import io.mockk.verify
import io.mockk.verifyOrder
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class CalculatorTest {

    lateinit var calculator: Calculator
    @BeforeEach
    fun setUp() {
        calculator = Calculator()
    }

    @Test
    fun increment() {
        // given
        val expected = 6

        // when
        val actual = calculator.increment(5)

        // then
        assertEquals(expected, actual)
    }

    @Test
    internal fun `stub increment`() {
        // given
        val mockCalculator = mockk<Calculator>(relaxed = true)
        every { mockCalculator.increment((5)) } returns 30

        // when
        val actual_result = mockCalculator.increment(5)

        // then
        assertEquals(30, actual_result)
    }

    @Test
    fun `stub mock increment test`() {
        // given
        val mockCalculator = mockk<Calculator>(relaxed = true)
        every { mockCalculator.increment((5)) } returns 30

        // when
        val actual_result = mockCalculator.increment(5)

        // then
        assertEquals(30, actual_result)

        // mocking
        // 1. 함수가 호출되었는지 여부 확인
        // 3. 어떤 인자로 함수가 호출되었는지 여부 확인
        verify { mockCalculator.increment(5) }

        // 2.함수가 몇번 호출되었는지 확인
        verify(exactly = 1) { mockCalculator.increment(5) }

        // 4. 인자가 특정 순서로 함수가 호출되었는지 확인
        verifyOrder { mockCalculator.increment(5) }
    }

    @Test
    fun decrement() {
        // given
        val expected = 6

        // when
        val actual = calculator.decrement(7)

        // then
        assertEquals(expected, actual)
    }

    @Test
    fun `stub decrement`() {
        // given
        val mockCalculator = mockk<Calculator>(relaxed = true)
        every { mockCalculator.decrement(5) } returns 30
        every { mockCalculator.decrement(4) } returns 30

        // when
        val actual_result = mockCalculator.decrement(4)

        // then
        assertEquals(30, actual_result)
    }

    @Test
    fun `stub mock decrement test`() {
        // given
        val mockCalculator = mockk<Calculator>(relaxed = true)
        every { mockCalculator.decrement(5) } returns 30

        // when
        val actual_result = mockCalculator.decrement(5)

        // then
        assertEquals(30, actual_result)

        // 1. 함수가 호출되었는지 여부 확인
        // 2.함수가 몇번 호출되었는지 확인
        // 3. 어떤 인자로 함수가 호출되었는지 여부 확인
        verify(exactly = 1) { mockCalculator.decrement(5) }

        // 4. 인자가 특정 순서로 함수가 호출되었는지 확인
        verifyOrder { mockCalculator.decrement(5) }
    }
}