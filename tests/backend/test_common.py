import keras.backend
import numpy
import numpy.testing

import keras_rcnn.backend


def test_anchor():
    x = numpy.array(
      [[ -84.,  -40.,  99.,  55.],
       [-176.,  -88., 191., 103.],
       [-360., -184., 375., 199.],
       [ -56.,  -56.,  71.,  71.],
       [-120., -120., 135., 135.],
       [-248., -248., 263., 263.],
       [ -36.,  -80.,  51.,  95.],
       [ -80., -168.,  95., 183.],
       [-168., -344., 183., 359.]]
    )

    x = keras.backend.variable(x)

    y = keras_rcnn.backend.anchor()

    x = keras.backend.eval(x)
    y = keras.backend.eval(y)

    numpy.testing.assert_array_equal(x, y)


def test_clip():
    pass
