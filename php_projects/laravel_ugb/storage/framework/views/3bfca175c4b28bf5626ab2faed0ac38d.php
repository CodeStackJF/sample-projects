<?php if (isset($component)) { $__componentOriginal23a33f287873b564aaf305a1526eada4 = $component; } ?>
<?php if (isset($attributes)) { $__attributesOriginal23a33f287873b564aaf305a1526eada4 = $attributes; } ?>
<?php $component = Illuminate\View\AnonymousComponent::resolve(['view' => 'components.layout','data' => []] + (isset($attributes) && $attributes instanceof Illuminate\View\ComponentAttributeBag ? $attributes->all() : [])); ?>
<?php $component->withName('layout'); ?>
<?php if ($component->shouldRender()): ?>
<?php $__env->startComponent($component->resolveView(), $component->data()); ?>
<?php if (isset($attributes) && $attributes instanceof Illuminate\View\ComponentAttributeBag): ?>
<?php $attributes = $attributes->except(\Illuminate\View\AnonymousComponent::ignoredParameterNames()); ?>
<?php endif; ?>
<?php $component->withAttributes([]); ?>
    <div class="row">
        <div class="col-md-3 form-group">
            <label>First name</label>
            <p><?php echo e($client->first_name); ?></p>
        </div>
        <div class="col-md-3 form-group">
            <label>Last name</label>
            <p><?php echo e($client->last_name); ?></p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-3 form-group">
            <label>Email</label>
            <p><?php echo e($client->email); ?></p>
        </div>
        <div class="col-md-2 form-group">
            <label>Phone Number</label>
            <p><?php echo e($client->phone_number); ?></p>
        </div>
    </div>
    <br>
    <div class="row">
        <div class="col-md-2 form-group"><a href="/clients" type="reset" class="btn btn-warning form-control">Return</a></div>
    </div>
 <?php echo $__env->renderComponent(); ?>
<?php endif; ?>
<?php if (isset($__attributesOriginal23a33f287873b564aaf305a1526eada4)): ?>
<?php $attributes = $__attributesOriginal23a33f287873b564aaf305a1526eada4; ?>
<?php unset($__attributesOriginal23a33f287873b564aaf305a1526eada4); ?>
<?php endif; ?>
<?php if (isset($__componentOriginal23a33f287873b564aaf305a1526eada4)): ?>
<?php $component = $__componentOriginal23a33f287873b564aaf305a1526eada4; ?>
<?php unset($__componentOriginal23a33f287873b564aaf305a1526eada4); ?>
<?php endif; ?><?php /**PATH D:\GIT\AplicacionesSeguras\sample-projects\php_projects\ugb\resources\views/clients/view.blade.php ENDPATH**/ ?>