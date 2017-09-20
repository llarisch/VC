git submodule update --init --recursive
cd TdVC
sh bootstrap
./configure
cd pyTdVC
sh execute_me.sh
python test_apps.py
