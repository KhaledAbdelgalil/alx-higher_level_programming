#include "Python.h"
/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
 * Compile with:
 * gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared
 * -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.8
 * 100-print_python_list_info.c
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t idx, list_size;
	PyObject *item;
	PyListObject *list = (PyListObject*)p;

	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) list_size);
	printf("[*] Allocated = %d\n", (int)list->allocated);
	for (idx = 0; idx < list_size; idx++)
	{
		item = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", (int) idx, item->ob_type->tp_name);
	}
}
