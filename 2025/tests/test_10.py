from day10 import transform_state

def test_transforming_state():
    #Arrange
    state = (0, 1, 1)
    button_seq = (0, 2)
    target_state = (1, 1, 0)

    # Act
    next_state =  transform_state(state, button_seq)

    # Assert
    assert next_state == target_state
