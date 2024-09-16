#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints some basic
 * info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int x;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (x = 0; x < Py_SIZE(p); x++)
		printf("Element %d: %s\n", x, Py_TYPE(PyList_GetItem(p, x))->tp_name);
}

