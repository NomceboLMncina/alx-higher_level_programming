#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *task, *prev = NULL;

	while (node)
	{
		task = node->task;
		node->task = prev;
		prev = node;
		node = task;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: If the linked list is not a palindrome - 0.
 * If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, y;

	if (*head == NULL || (*head)->task == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->task;
	}

	tmp = *head;
	for (y = 0; y < (size / 2) - 1; y++)
		tmp = tmp->task;

	if ((size % 2) == 0 && tmp->x != tmp->task->x)
		return (0);

	tmp = tmp->task->task;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->x != rev->x)
			return (0);
		tmp = tmp->task;
		rev = rev->task;
	}
	reverse_listint(&mid);

	return (1);
}
