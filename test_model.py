from model import make_prediction

def test_prediction_logic():
    # We pass 5 to our model. We EXPECT the answer to be 10.
    result = make_prediction(5)
    assert result == 10  # If result is not 10, the test fails
