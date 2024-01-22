#include <Python.h>
#include <stdio.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	Py_ssize_t list_size = 0;
	PyObject *current_element;
	int idx = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		list_size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", list_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (;idx < list_size; idx++)
		{
			current_element = PyList_GET_ITEM(p, idx);
			printf("Element %d: %s\n", idx, current_element->ob_type->tp_name);
			if (PyBytes_Check(current_element))
				print_python_bytes(current_element);
			else if (PyFloat_Check(current_element))
				print_python_float(current_element);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}

}



void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (((PyBytesObject *)(p))->ob_sval);
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	double value = 0;
	char *value_str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	value_str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", value_str);
}
