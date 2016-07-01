import tensorflow as tf

graph = tf.get_default_graph()

input_value = tf.constant(1.0)

operations = graph.get_operations()
print operations[0].node_def

print input_value

sess = tf.Session()
sess.run(input_value)

weight = tf.Variable(0.8)

for op in graph.get_operations(): print op.name

output_value = weight * input_value

op = graph.get_operations()[-1]
print op.name

for op_input in op.inputs: print op_input

init = tf.initialize_all_variables()
sess.run(init)

sess.run(output_value)

x = tf.constant(1.0, name='input')
w = tf.Variable(0.8, name='weight')
y = tf.mul(w, x, name='output')

summary_writer = tf.train.SummaryWriter('log_simple_graph', sess.graph)