#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - function in C that inserts a number into a sorted
 * singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: number to insert.
 * Return: address of the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t new_node = malloc(sizeof(listint_t node));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = head;
	*head = new_node;

	return (new_node);
}
