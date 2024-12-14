import tensorflow as tf

# print(tf.version)

# string = tf.Variable("this is string")
# integer = tf.Variable(231)
# floating = tf.Variable(23.231)

# print(string)
# print(integer)
# print(floating)

# rank1 = tf.Variable([123,12124,12314])
# rank2 = tf.Variable([[12,412],[213,231]])

# print(rank1)
# print(rank2)

rank3 = tf.Variable([[12,412],[213,231],[213,213],[231,312]])
# print(rank3)
tf.rank(rank3)