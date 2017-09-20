mkdir .deps

cython --cplus ExpVC.pyx -o ExpVC.cpp

../libtool  --tag=CXX   --mode=compile g++ -DPACKAGE_NAME=\"VC\" -DPACKAGE_TARNAME=\"VC\" -DPACKAGE_VERSION=\"0.1.0\" -DPACKAGE_STRING=\"ExpVC\ 0.1.0\" -DPACKAGE=\"ExpVC\" -DVERSION=\"0.1.0\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DLT_OBJDIR=\".libs/\" -I.  -I/usr/include/python2.7 -I../src -DNDEBUG -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -fno-strict-aliasing -g -fwrapv -O2 -Wall -Wformat -Werror=format-security -g -O2 -std=c++11 -MT ExpVC.lo -MD -MP -MF .deps/ExpVC.Tpo -c -o ExpVC.lo ExpVC.cpp

g++ -DPACKAGE_NAME=\"ExpVC\" -DPACKAGE_TARNAME=\"ExpVC\" -DPACKAGE_VERSION=\"0.1.0\" "-DPACKAGE_STRING=\"ExpVC 0.1.0\"" -DPACKAGE=\"tdlib\" -DVERSION=\"0.1.0\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DLT_OBJDIR=\".libs/\" -I. -I/usr/include/python2.7 -I../src -DNDEBUG -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -fno-strict-aliasing -g -fwrapv -O2 -Wall -Wformat -Werror=format-security -g -O2 -std=c++11 -MT ExpVC.lo -MD -MP -MF .deps/ExpVC.Tpo -c ExpVC.cpp  -fPIC -DPIC -o .libs/ExpVC.o

g++ -DPACKAGE_NAME=\"ExpVC\" -DPACKAGE_TARNAME=\"ExpVC\" -DPACKAGE_VERSION=\"0.1.0\" "-DPACKAGE_STRING=\"ExpVC 0.1.0\"" -DPACKAGE=\"ExpVC\" -DVERSION=\"0.1.0\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DLT_OBJDIR=\".libs/\" -I. -I/usr/include/python2.7 -I../src -DNDEBUG -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -fno-strict-aliasing -g -fwrapv -O2 -Wall -Wformat -Werror=format-security -g -O2 -std=c++11 -MT ExpVC.lo -MD -MP -MF .deps/ExpVC.Tpo -c ExpVC.cpp -o ExpVC.o >/dev/null 2>&1

mv -f .deps/ExpVC.Tpo .deps/ExpVC.Plo

../libtool  --tag=CXX   --mode=compile g++ -DPACKAGE_NAME=\"ExpVC\" -DPACKAGE_TARNAME=\"ExpVC\" -DPACKAGE_VERSION=\"0.1.0\" -DPACKAGE_STRING=\"tdlib\ 0.1.0\" -DPACKAGE=\"ExpVC\" -DVERSION=\"0.1.0\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DLT_OBJDIR=\".libs/\" -I.  -I/usr/include/python2.7 -I../src -DNDEBUG -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -fno-strict-aliasing -g -fwrapv -O2 -Wall -Wformat -Werror=format-security -g -O2 -std=c++11 -MT python_ExpVC.lo -MD -MP -MF .deps/python_ExpVC.Tpo -c -o python_ExpVC.lo python_ExpVC.cpp

g++ -DPACKAGE_NAME=\"ExpVC\" -DPACKAGE_TARNAME=\"ExpVC\" -DPACKAGE_VERSION=\"0.1.0\" "-DPACKAGE_STRING=\"ExpVC 0.1.0\"" -DPACKAGE=\"ExpVC\" -DVERSION=\"0.1.0\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DLT_OBJDIR=\".libs/\" -I. -I/usr/include/python2.7 -I../src -DNDEBUG -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -fno-strict-aliasing -g -fwrapv -O2 -Wall -Wformat -Werror=format-security -g -O2 -std=c++11 -MT python_ExpVC.lo -MD -MP -MF .deps/python_ExpVC.Tpo -c python_ExpVC.cpp  -fPIC -DPIC -o .libs/python_ExpVC.o

g++ -DPACKAGE_NAME=\"ExpVC\" -DPACKAGE_TARNAME=\"ExpVC\" -DPACKAGE_VERSION=\"0.1.0\" "-DPACKAGE_STRING=\"ExpVC 0.1.0\"" -DPACKAGE=\"ExpVC\" -DVERSION=\"0.1.0\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DLT_OBJDIR=\".libs/\" -I. -I/usr/include/python2.7 -I../src -DNDEBUG -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -fno-strict-aliasing -g -fwrapv -O2 -Wall -Wformat -Werror=format-security -g -O2 -std=c++11 -MT python_ExpVC.lo -MD -MP -MF .deps/python_ExpVC.Tpo -c python_ExpVC.cpp -o python_ExpVC.o >/dev/null 2>&1

mv -f .deps/python_ExpVC.Tpo .deps/python_ExpVC.Plo

../libtool  --tag=CXX   --mode=link g++ -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -fno-strict-aliasing -g -fwrapv -O2 -Wall -Wformat -Werror=format-security -g -O2 -std=c++11 -module -omit-version  -o ExpVC.la -rpath /usr/local/lib/python2.7/dist-packages/ExpVC ExpVC.lo python_ExpVC.lo  

g++  -fPIC -DPIC -shared -nostdlib /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/5/crtbeginS.o  .libs/ExpVC.o .libs/python_ExpVC.o   -L/usr/lib/gcc/x86_64-linux-gnu/5 -L/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/lib/gcc/x86_64-linux-gnu/5/../../.. -lstdc++ -lm -lc -lgcc_s /usr/lib/gcc/x86_64-linux-gnu/5/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/crtn.o  -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -g -O2 -g -O2   -pthread -Wl,-soname -Wl,ExpVC.so.0 -o .libs/ExpVC.so.0.0.0

cd ".libs" && rm -f "ExpVC.so.0" && ln -s "ExpVC.so.0.0.0" "ExpVC.so.0"

cd ..

cd ".libs" && rm -f "ExpVC.so" && ln -s "ExpVC.so.0.0.0" "ExpVC.so"

cd ..

ar cru .libs/ExpVC.a  ExpVC.o python_ExpVC.o

cp .libs/ExpVC.so .
