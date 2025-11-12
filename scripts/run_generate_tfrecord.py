import sys, runpy
# Ensure TF1-style gfile exists for older object_detection utils
try:
    import tensorflow as _tf
    if not hasattr(_tf, "gfile"):
        _tf.gfile = _tf.io.gfile
except Exception:
    pass

# Forward CLI args to original script
orig = r"C:\RealTimeObjectDetection\Tensorflow\scripts\generate_tfrecord.py"
sys.argv = [orig] + sys.argv[1:]
runpy.run_path(orig, run_name="__main__")
