include "lists.h"

/**
 *is_palindrome - checks is singly linked list is palindrome
 *@head:adress
 *
 *Return:0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || head->next == NULL)
	{
		return (1);
	}

