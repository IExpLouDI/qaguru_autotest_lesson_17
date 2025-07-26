import os.path

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR)))
SCHEMAS_DIR = os.path.join(ROOT_DIR, 'src', 'qaguru_autotest_lesson_17', 'schemas')
