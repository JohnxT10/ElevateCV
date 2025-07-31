from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CV
from .forms import CVForm

@login_required
def cv_list(request):
    cvs = CV.objects.filter(user=request.user)
    return render(request, 'cvbuilder/cv_list.html', {'cvs': cvs})

@login_required
def cv_create(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            return redirect('cv_list')
    else:
        form = CVForm()
    return render(request, 'cvbuilder/cv_form.html', {'form': form})

@login_required
def cv_edit(request, pk):
    cv = get_object_or_404(CV, pk=pk, user=request.user)
    form = CVForm(request.POST or None, instance=cv)
    if form.is_valid():
        form.save()
        return redirect('cv_list')
    return render(request, 'cvbuilder/cv_form.html', {'form': form})

@login_required
def cv_delete(request, pk):
    cv = get_object_or_404(CV, pk=pk, user=request.user)
    if request.method == 'POST':
        cv.delete()
        return redirect('cv_list')
    return render(request, 'cvbuilder/cv_confirm_delete.html', {'cv': cv})


def public_cv_builder(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                cv = form.save(commit=False)
                cv.user = request.user
                cv.save()
                return redirect('cv_list')
            else:
                # For now, just show a preview; later, add PDF generation
                return render(request, 'cvbuilder/cv_pdf_preview.html', {'form': form, 'data': form.cleaned_data})
    else:
        form = CVForm()
    return render(request, 'cvbuilder/public_cv_form.html', {'form': form})