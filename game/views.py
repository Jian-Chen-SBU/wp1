from django.shortcuts import render, redirect
from .forms import SignInForm
from django.utils import timezone
import json
import urllib.request
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def process_grid(grid):
	for i in range(0, len(grid)):
		if(grid[i] == " "):
			grid[i] = "O"
			return grid

def get_winner(grid):
	if(grid[0] == grid[1] and grid[1] == grid[2] and grid[0] != " "):
		return grid[0]		
	elif(grid[3] == grid[4] and grid[4] == grid[5] and grid[3] != " "):
		return grid[3]
	elif(grid[6] == grid[7] and grid[7] == grid[8] and grid[6] != " "):
		return grid[6]
	elif(grid[0] == grid[3] and grid[3] == grid[6] and grid[0] != " "):
		return grid[0]
	elif(grid[1] == grid[4] and grid[4] == grid[7] and grid[1] != " "):
		return grid[1]
	elif(grid[2] == grid[5] and grid[5] == grid[8] and grid[2] != " "):
		return grid[2]
	elif(grid[0] == grid[4] and grid[4] == grid[8] and grid[0] != " "):
		return grid[0]
	elif(grid[2] == grid[4] and grid[4] == grid[6] and grid[2] != " "):
		return grid[2]
	else:
		return " "

def isFull(grid):
	for i in range(0, len(grid)):
		if(grid[i] != " "):
			return False
	return True

@csrf_exempt
def form(request):
	if request.method == 'POST':
		form = SignInForm(request.POST)
		if form.is_valid():
			# sanitize the input for name
			name = form.cleaned_data['name']		
			now = timezone.now()
			context = {'name' : name, 'date' : now}			
			return render(request, 'ttt.html', context)

	else:
		form = SignInForm()				
		context = {'form' : form}
		return render(request, 'form.html', context)
 
@csrf_exempt
def game(request):
	if request.method == 'POST':
		data = json.loads(request.body.decode())
		grid = data['grid']		
		winner = get_winner(grid)	
		if(winner == " "):
			grid = process_grid(grid)
		winner = get_winner(grid)		
		json_data = {
			"grid" : grid,
			"winner" : winner
		}
		return JsonResponse(json_data)
		
