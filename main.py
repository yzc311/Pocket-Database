import os
import pytest


pytest.main()

os.system('allure generate -c -o report temps')