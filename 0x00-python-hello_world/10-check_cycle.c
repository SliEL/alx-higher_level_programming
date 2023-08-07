#include "lists.h"

/**
 * check_cycle - checks if the ll contains a cycle
 * @list: the LL to check
 *
 * Return: 1 if it contains a cycle and 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
