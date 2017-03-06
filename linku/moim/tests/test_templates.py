from moim.models import Meeting
import pytest
import datetime


@pytest.mark.django_db
def test_homepage_use_sign_up_template(client):
    response_templates = client.get('/signup/').templates
    assert 'sign_up.html' in (
        template.name for template in response_templates)


@pytest.mark.django_db
def test_homepage_use_meeting_list_template(client):
    response_templates = client.get('/').templates
    assert 'meeting_list.html' in (
        template.name for template in response_templates)


@pytest.mark.django_db
def test_apply_meeting_view_use_correct_template(client):
    meeting = Meeting.objects.create(maker='test maker', name='test name', place='test place',
                                     start_time=datetime.datetime.now(),
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')
    response_templates = client.get('/meetings/' + str(meeting.id) + '/apply/').templates
    assert 'apply_meeting.html' in (
        template.name for template in response_templates)


@pytest.mark.django_db
def test_enter_specific_moim_page_use_specific_moim_template(client):
    meeting = Meeting.objects.create(maker='test maker', name='test name', place='test place',
                                     start_time=datetime.datetime.now(),
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')
    response_templates = client.get('/meetings/' + str(meeting.id) + '/').templates
    assert 'specific_moim.html' in (
        template.name for template in response_templates
    )
