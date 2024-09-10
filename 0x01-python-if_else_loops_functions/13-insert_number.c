#include "lists.h"

/**
 * insert_node - inserts a node sorted in a linked list of ints
 * @head: double pointer to head of LL, needed for modification in edge
 * cases
 * @number: data for new node
 * Return: pointer to new node, or NULL if fail
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *data;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || (*head)->n >= new->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		data = *head;
		while (data->next != NULL && data->next->n < new->n)
			data = data->next;
		new->next = data->next;
		data->next = new;
	}
	return (*head);
}

