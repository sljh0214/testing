import calculator

def test_crement():
    # given (expected_result)
    expected_result = 5

    # when (actual_result)
    actual_result = calculator.increment(4)

    # then (expected_result == actual_result)
    assert expected_result == actual_result

def test_stub_increment(mocker):
    # given (preparing, expected)
    expected_result = 30
    mocker.patch('calculator.increment', return_value=30)

    # when
    actual_result = calculator.increment(4)

    # then
    assert expected_result == actual_result

def test_stub_mock_increment(mocker):
    # given (preparing, expected)
    expected_result = 30
    mocked_increment = mocker.patch('calculator.increment', return_value=30)

    # when
    actual_result = calculator.increment(30)

    # then (verify)
    assert expected_result == actual_result
    # mocking
    # 1. 함수가 호출되었는지 여부 확인
    mocked_increment.assert_called()

    # 2. 함수가 몇번 호출되었는지 검증
    assert mocked_increment.call_count == 1

    # 3. 어떤 인자로 함수가 호출되었는지 확인
    assert mocked_increment.call_args == mocker.call(30)

    # 4. 인자가 특정 순서로 함수가 호출되었는지 확인
    assert mocked_increment.call_args_list == [mocker.call(30)]

def test_decrement():
    # given
    expected_result = 5

    # when
    actual_result = calculator.decrement(6)

    # then
    assert expected_result == actual_result


def test_stub_decrement(mocker):
    # given (preparing, expected)
    expected_result = 30
    mocker.patch('calculator.decrement', return_value=30)

    # when
    actual_result = calculator.decrement(6)

    # then
    assert expected_result == actual_result

def test_stub_mock_decrement(mocker):
    # given (preparing, expected)
    expected_result = 30
    mocked_increment = mocker.patch('calculator.decrement', return_value=30)

    # when
    actual_result = calculator.decrement(6)

    # then
    assert expected_result == actual_result
    # mocking
    # 1. 함수가 호출되었는지 여부 확인
    mocked_increment.assert_called()

    # 2. 함수가 몇번 호출되었는지 검증
    assert mocked_increment.call_count == 1

    # 3. 어떤 인자로 함수가 호출되었는지 확인
    assert mocked_increment.call_args == mocker.call(6)

    # 4. 인자가 특정 순서로 함수가 호출되었는지 확인
    assert mocked_increment.call_args_list == [mocker.call(6)]