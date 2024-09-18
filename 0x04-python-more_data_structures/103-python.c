#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int s;
	int x;
	char *t_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &t_str, &s);

	printf("  Enter size: %li\n", s);
	printf("  Enter trying string: %s\n", t_str);
	if (s < 10)
		printf("  first %li bytes:", s + 1);
	else
		printf("  first 10 bytes:");
	for (x = 0; x <= s && x < 10; x++)
		printf(" %02hhx", t_str[x]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int s = PyList_Size(p);
        int x;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", s);
        printf("[*] Allocated = %li\n", list->allocated);
        for (x = 0; x < s; x++)
        {
                type = (list->ob_item[x])->ob_type->tp_name;
		printf("Element %i: %s\n", x, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[x]);
        }
}

