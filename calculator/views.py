from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time

def index(request):
    return render(request, 'calculator/index.html')

@csrf_exempt
def calculate_future_value(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            monthly_investment = float(data.get('monthly_investment', 0))
            yearly_rate = float(data.get('yearly_rate', 0))
            years = int(data.get('years', 0))
            
            # Future Value calculation
            monthly_rate = yearly_rate / 100 / 12
            total_months = years * 12
            
            if monthly_rate == 0:
                future_value = monthly_investment * total_months
            else:
                future_value = monthly_investment * (((1 + monthly_rate) ** total_months - 1) / monthly_rate)
            
            # Simulate server processing time for animation effect
            time.sleep(0.5)
            
            return JsonResponse({
                'success': True,
                'future_value': round(future_value, 2),
                'calculation_steps': {
                    'monthly_investment': monthly_investment,
                    'yearly_rate': yearly_rate,
                    'years': years,
                    'total_months': total_months,
                    'monthly_rate': round(monthly_rate * 100, 4)
                }
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
