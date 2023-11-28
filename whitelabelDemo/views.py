from django.shortcuts import render



# Create your views here.
def WhiteLabelView(request):
    
    subdomain = request.subdomain
    
    print("request ",request.META['HTTP_HOST'])
    print("request ",request.META['HTTP_HOST'].split('.')[0])
    
    return render(request, 'whitelabelDemo/whitelabel.html',context={'data':subdomain})