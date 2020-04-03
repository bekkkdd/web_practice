from django.http.response import HttpResponse, JsonResponse

from api.models import Company, Vacancy


def company_list(request):
    companies = Company.objects.all()
    company_json = [company.to_json() for company in companies]
    return JsonResponse(company_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company doesn`t exist'})
    return JsonResponse(company.to_json())


def vacancy_from_company(request, company_id):
    vacancies = Vacancy.objects.all()
    vacancy = []
    for vac in vacancies:
        a = vac.to_json()
        if a['company_id'] == company_id:
            vacancy.append(a)

    if len(vacancy):
        return JsonResponse(vacancy, safe=False)
    else:
        return HttpResponse("Error I cannot found smthg")


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': 'Vacancy doesn`t exist'})
    return JsonResponse(vacancy.to_json())


def top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10:1]
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)
