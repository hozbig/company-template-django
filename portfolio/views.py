from django.shortcuts import render
from .models import Portfolio


# blog_home view
def portfolio_home_view(request):
	portfolios = Portfolio.objects.all().filter(status = "p")
	context = {
		"page_title": "نمونه کارها",
		"portfolios": portfolios,
	}
	return render(request, 'portfolio/portfolio-home.html', context)


# portfolio_post view
def portfolio_post_view(request, slug):
	try:
		portfolio = Portfolio.objects.all().get(slug=slug)
		templateName = 'portfolio/portfolio-post.html'
	except:
		portfolio = None
		templateName = "portfolio/portfolio-post.html"
	context = {
		"page_title": portfolio.title,
		"portfolio": portfolio,
	}
	return render(request, templateName, context)