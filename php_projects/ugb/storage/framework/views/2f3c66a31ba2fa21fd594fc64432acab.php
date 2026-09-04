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
    <h1>Clients</h1>

     <?php $__env->slot('name', null, []); ?> 
        Pedro
     <?php $__env->endSlot(); ?>

    <div class="container">
        <form method="post" action="/clients">
            <div class="row">
                <div class="col-md-3 form-group">
                    <label>First name</label>
                    <input type="text" class="form-control" name="first_name" value="<?php echo e(old('first_name')); ?>">
                    <?php $__errorArgs = ['first_name'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                        <div class="label">
                            <span class=""><?php echo e($message); ?></span>
                        </div>
                    <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
                </div>
                <div class="col-md-3 form-group">
                    <label>Last name</label>
                    <input type="text" class="form-control" name="last_name" value="<?php echo e(old('last_name')); ?>">
                    <?php $__errorArgs = ['last_name'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                        <div class="label">
                            <span class=""><?php echo e($message); ?></span>
                        </div>
                    <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 form-group">
                    <label>Email</label>
                    <input type="text" class="form-control" name="email" value="<?php echo e(old('email')); ?>">
                    <?php $__errorArgs = ['email'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                        <div class="label">
                            <span class=""><?php echo e($message); ?></span>
                        </div>
                    <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
                </div>
                <div class="col-md-2 form-group">
                    <label>Phone Number</label>
                    <input type="text" class="form-control" name="phone_number" value="<?php echo e(old('phone_number')); ?>">
                    <?php $__errorArgs = ['phone_number'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                        <div class="label">
                            <span class=""><?php echo e($message); ?></span>
                        </div>
                    <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-md-2 form-group"><button type="submit" class="btn btn-primary form-control">Add</button></div>
                <div class="col-md-2 form-group"><button type="reset" class="btn btn-warning form-control">Reset</button></div>
            </div>
        </form>
    </div>
    <br>
    <div class="row">
        <?php $__currentLoopData = $clients; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $client): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
        <div class="card">
            <div class="card-header">
                <?php echo e($client->first_name); ?> <?php echo e($client->last_name); ?>

            </div>
            <div class="card-body">
                <h5 class="card-title"><?php echo e($client->email); ?></h5>
                <p class="card-text">Phone Number: <?php echo e($client->phone_number); ?></p>
                <ul>
                    <?php $__currentLoopData = $client->phoneNumbers; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $phone_number): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
                        <li>(<?php echo e($phone_number->area_code); ?>) <?php echo e($phone_number->phone); ?></li>
                    <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?>
                </ul>
                <small>Created at: <?php echo e($client->created_at); ?> | Updated at: <?php echo e($client->updated_at); ?></small>
                <hr>
                <a href="/clients/<?php echo e($client->id); ?>/view" class="btn btn-primary">View</a>
                <a href="/clients/<?php echo e($client->id); ?>/edit" class="btn btn-primary">Edit</a>
                <a href="/clients/<?php echo e($client->id); ?>/delete" class="btn btn-primary">Delete</a>
            </div>
            </div>
        <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?>
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
<?php endif; ?><?php /**PATH D:\GIT\AplicacionesSeguras\sample-projects\php_projects\ugb\resources\views/clients/index.blade.php ENDPATH**/ ?>