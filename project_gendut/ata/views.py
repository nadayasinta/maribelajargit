from django.shortcuts import render

# Create your views here.
def inputmentor(request):
    if request.method == 'POST':
        form = Input_Mentor(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect('halaman_mentor')

    else:
        form = Input_Mentor()
    return render(request, 'input_mentor.html',{'form':form})