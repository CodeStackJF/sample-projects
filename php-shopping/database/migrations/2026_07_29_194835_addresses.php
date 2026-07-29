<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
         if (!Schema::hasTable('addresses')) {
            Schema::create('addresses', function(Blueprint $table) {
                $table->id('id');
                $table->integer('client_id');
                $table->foreign('client_id')->references('id')->on('clients')->onDelete('cascade');
                $table->string('street', 50);
                $table->string('avenue', 50);
                $table->boolean('active')->default(false);
                $table->timestamps();
            });
        }
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        //
    }
};
