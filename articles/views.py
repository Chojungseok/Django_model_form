from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles
    }
    return render(request, 'index.html', context)

def create(request):
    # new/ = 빈 종이를 보여주는 기능
    # create/ = 사용자가 입력한 데이터 저장
    # -------------------------------
    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 사용자가 입력한 데이터 저장
    # -------------------------------
    ## 모든 경우의 수
    ## 1. GET: form을 만들어서 html문서를 사용자에게 리턴
    ## 2. POST: 
    ##      2-1. invalid data(데이터 검증 실패)
    ##      2-2. valid data(데이터 검증 성공)
    
    # 5. Post 요청(invalid data)
    # 10. POST 요청(valid data)
    if request.method == 'POST':
        # 6. 사용자가 입력한 데이터(request.POST)를 담은 form 생성(invalid)
        # 11. 사용자가 입력한 데이터(request.POST)를 담은 form 생성(valid)
        form = ArticleForm(request.POST)
        # 7. form을 검증(실패)
        # 12. form을 검증(성공)
        if form.is_valid():
            form.save()
            # 13. index로 redirect
            return redirect('articles:index')
    else: # 1. GET 요청
        form = ArticleForm() # 2. 비어있는 Form을 만든다
    # 3. context dict에 비어있는 form을 담는다
    # 8. context dict에 검증에 실패한 form을 담는다
    context = { 
        'form' : form,
    }
    # 4. create.html을 랜더링
    # 9. create.html 랜더링
    return render(request, 'create.html', context)