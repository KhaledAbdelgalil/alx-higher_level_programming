#include "lists.h"

listint_t* reverse_list(listint_t * list)
{
	listint_t* prev = NULL, *current = list, *nextNode = NULL;
	while (current)
	{
		nextNode = current->next;
		current->next = prev;
		prev = current;
		current = nextNode;
	}
	return (prev);
}
int compare_lists(listint_t* list1, listint_t* list2) {
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
		{
			return (0);
		}
		list1 = list1->next;
		list2 = list2->next;
	}
	return (1);
}
int is_palindrome(listint_t **head)
{
	listint_t* slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *midNode = NULL, *secondHalf = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (0);
	while (fast != NULL && fast->next != NULL)
	{
		prev_slow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
	{
		midNode = slow;
		slow = slow->next;
	}
	secondHalf = reverse_list(slow);
	palindrome = compare_lists(*head, secondHalf);
	secondHalf = reverse_list(secondHalf);
	if (midNode != NULL)
	{
		prev_slow->next = midNode;
		midNode->next = secondHalf;
	}
	else 
	{
		prev_slow->next = secondHalf;
	}

	return (palindrome);
}
   
