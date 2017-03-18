# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 08:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('job_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='作业名称')),
                ('deploy_status', models.IntegerField(blank=True, choices=[(0, '部署中'), (1, '部署完成'), (2, '部署失败')], default=0, null=True, verbose_name='部署状态')),
            ],
            options={
                'verbose_name': '历史作业',
                'verbose_name_plural': '历史作业',
            },
        ),
        migrations.CreateModel(
            name='DeployJobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('deploy_message', models.TextField(blank=True, null=True, verbose_name='作业信息')),
                ('job_cmd', models.TextField(blank=True, null=True, verbose_name='作业命令')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('duration', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='执行时长')),
                ('stderr', models.TextField(blank=True, null=True, verbose_name='其他信息')),
                ('comment', models.TextField(blank=True, default='', null=True, verbose_name='提示信息')),
                ('is_success', models.BooleanField(choices=[(True, '执行成功'), (False, '执行失败')], default=True, verbose_name='执行情况')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Host', verbose_name='主机名')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.DeployJob', verbose_name='作业名称')),
            ],
            options={
                'verbose_name': '部署详情',
                'verbose_name_plural': '部署详情',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='业务名称')),
                ('job_script_type', models.IntegerField(choices=[(100, '----'), (0, 'sls'), (1, 'shell')], default=0, verbose_name='脚本语言')),
                ('playbook', models.TextField(blank=True, help_text='${version}代表默认版本号', null=True, verbose_name='部署脚本')),
                ('anti_install_playbook', models.TextField(blank=True, help_text='${version}代表默认版本号', null=True, verbose_name='卸载脚本')),
                ('extra_param', models.TextField(blank=True, default='', null=True, verbose_name='扩展参数')),
                ('backup_monitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backup_monitor', to=settings.AUTH_USER_MODEL, verbose_name='备份负责人')),
                ('dev_monitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dev_monitor', to=settings.AUTH_USER_MODEL, verbose_name='开发负责人')),
            ],
            options={
                'verbose_name': '业务',
                'verbose_name_plural': '业务',
            },
        ),
        migrations.CreateModel(
            name='ProjectConfigFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('config_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='配置文件路径')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.Project', verbose_name='业务')),
            ],
            options={
                'verbose_name': '业务配置',
                'verbose_name_plural': '业务配置',
            },
        ),
        migrations.CreateModel(
            name='ProjectHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Host', verbose_name='主机')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.Project', verbose_name='业务')),
            ],
            options={
                'verbose_name': '业务主机',
                'verbose_name_plural': '业务主机',
            },
        ),
        migrations.CreateModel(
            name='ProjectHostConfigFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('file_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='配置路径')),
                ('file_content', models.TextField(blank=True, null=True, verbose_name='配置内容')),
                ('project_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.ProjectHost', verbose_name='业务')),
            ],
            options={
                'verbose_name': '配置内容',
                'verbose_name_plural': '配置内容',
            },
        ),
        migrations.CreateModel(
            name='ProjectModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='业务模块名称')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='deploy_manager.ProjectModule', verbose_name='上级业务模块')),
            ],
            options={
                'verbose_name': '业务模块',
                'verbose_name_plural': '业务模块',
            },
        ),
        migrations.CreateModel(
            name='ProjectVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='版本名称')),
                ('files', models.FileField(blank=True, null=True, upload_to='/Users/kira/oschina/saltops/doc/script/', verbose_name='版本')),
                ('is_default', models.BooleanField(default=False, verbose_name='默认版本')),
                ('subplaybook', models.TextField(blank=True, help_text='为空则使用全局的部署脚本', null=True, verbose_name='部署脚本')),
                ('sub_job_script_type', models.IntegerField(choices=[(100, '----'), (0, 'sls'), (1, 'shell')], default=100, verbose_name='脚本语言')),
                ('extra_param', models.TextField(blank=True, default='', null=True, verbose_name='扩展参数')),
                ('anti_install_playbook', models.TextField(blank=True, help_text='${version}代表默认版本号', null=True, verbose_name='卸载脚本')),
                ('project', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.Project', verbose_name='业务名称')),
            ],
            options={
                'verbose_name': '版本信息',
                'verbose_name_plural': '版本信息',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='host',
            field=models.ManyToManyField(blank=True, default='', through='deploy_manager.ProjectHost', to='cmdb.Host', verbose_name='主机'),
        ),
        migrations.AddField(
            model_name='project',
            name='ops_monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ops_monitor', to=settings.AUTH_USER_MODEL, verbose_name='运维负责人'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_module',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.ProjectModule', verbose_name='业务模块'),
        ),
        migrations.AddField(
            model_name='deployjob',
            name='project_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.ProjectVersion', verbose_name='版本'),
        ),
    ]