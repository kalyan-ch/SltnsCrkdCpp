#ifndef __LINKEDLIST_H_INCLUDED__
#define __LINKEDLIST_H_INCLUDED__
#endif

#include <iostream>
#include <vector>
#include <algorithm>
#include "Node.h"

using namespace std;

class LinkedList
{
	public:
		Node* head;
		LinkedList(){
			head = NULL;
		}
		void addNode(int val){
			Node* a = new Node(val);
			if(head==NULL){
				head = a;
			}else{
				Node* n = head;
				while(true){
					if(n->next == NULL){
						n->next = a;
						break;
					}
					n = n->next;
				}
				
			}
		}

		int listLength(){
			int count = 0;
			Node* n = head;
			while(n!=NULL){
				n = n->next;
				count += 1;
			}

			return count;
		}

		void rev_printList(Node* n){
			if(n==NULL){
				return;
			}
			rev_printList(n->next);
			cout<< n->data;
		}

		void printList(){
			Node* n = head;
			while(n!=NULL){
				if(n->next!=NULL){
			        cout << n->data << " -> ";    
			    }else{
			        cout << n->data;
			    }
				n = n->next;
			}
			cout << "\n";
		}

		void deleteNode(int val){
			if(head->data == val){
				head = head->next;
			}else{
				Node* n = head;
				while(n->next!=NULL){
					if(n->next->data == val){
						n->next = n->next->next;
						break;
					}
					n = n->next;
				}
			}
			
		}
	
};

