#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function to check the cycle of a linked list
 * @list: the linked list
 * Return: 1 if yes and 0 if no
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
