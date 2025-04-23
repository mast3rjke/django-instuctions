from django.http import HttpResponseRedirect
from django.shortcuts import render


def base_edit_page(request, form_class, model_class, entity_id):
    model = model_class.objects.get(pk=entity_id)
    form = form_class(instance=model)

    if request.method == "POST":
        form = form_class(request.POST)
        # Хук для получения полей модели
        fields = [
            str(i).split(".")[-1]
            for i in model._meta.fields
            if "." in str(i)
        ]
        if form.is_valid():
            for field_name in fields:
                # ИД у нас и так есть - не заполняем
                if field_name == "id":
                    continue

                setattr(model, field_name, form.cleaned_data[field_name])
            model.save()

    return render(request, "app_1/entity_form_page.html", {"form": form})


def base_create_page(request, form_class):
    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/")
    else:
        form = form_class()

    return render(
        request,
        "app_1/entity_form_page.html",
        {"form": form}
    )


def base_delete_entity(model_class, entity_id):
    model = model_class.objects.get(pk=entity_id)

    if model:
        model.delete()

    return HttpResponseRedirect("/")


def base_view(request, model_class, entity_id, entity_name, params):
    try:
        entity = model_class.objects.get(pk=entity_id)
    except model_class.DoesNotExist:
        entity = None

    # В параметрах ждем функцию получения заголовка
    title = params.get("header_creator")(entity)

    context = {
        "title": title,
        entity_name: entity
    }

    # Если передали дополнительные поля - засунем их в контекст
    for field in params.get("additional_data", []):
        context[field] = getattr(entity, field)

    return render(
        request, f"app_1/{entity_name}_view.html", context
    )
