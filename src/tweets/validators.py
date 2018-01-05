from django.core.exceptions import ValidationError


# Validation functions for model fields

def validate_content(value):
	content = value
	if content == "":
		raise ValidationError("Content cannot be blank")
	return value