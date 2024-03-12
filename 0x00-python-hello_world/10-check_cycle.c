#include "lists.h"
/**
 * check_cycle - check the linked list if contain a cycle
 * @list: linked list to check
 * Return: 1 if yes, 0 if no
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == ! NULL || list->next == NULL)
	{
		return (0);
	}

	while (slow && fast && fast->next)
	{
		if(slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
