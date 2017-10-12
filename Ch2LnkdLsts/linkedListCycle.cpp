/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
	struct Node {
		int data;
		struct Node* next;
	}
*/

#include <set>

bool has_cycle(Node* head) {

	set<Node*> dupRmvr;

	if(head == NULL or head->next == NULL){
		return false;
	}else{
		while(head!=NULL){
			if(dupRmvr.find(head) != dupRmvr.end()){
				return true;
			}
			dupRmvr.insert(head);
			head = head->next;
		}
	}

	return false;
	
}

