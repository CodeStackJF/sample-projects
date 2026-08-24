<?php

namespace App\Http\Controllers;

use App\Models\Clients;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Validation\Rule;

class ClientAPIController extends Controller
{
    public function index(): JsonResponse
    {
        return response()->json(['data' => Clients::all()]);
    }

    public function save(Request $request): JsonResponse
    {
        $client = Clients::create($this->validatedData($request));

        return response()->json([
            'message' => 'Client created successfully.',
            'data' => $client,
        ], 201);
    }

    public function view(Clients $client): JsonResponse
    {
        return response()->json(['data' => $client]);
    }

    public function update(Request $request, Clients $client): JsonResponse
    {
        $client->update($this->validatedData($request, $client));

        return response()->json([
            'message' => 'Client updated successfully.',
            'data' => $client->fresh(),
        ]);
    }

    public function delete(Clients $client): JsonResponse
    {
        $client->delete();

        return response()->json(['message' => 'Client deleted successfully.']);
    }

    private function validatedData(Request $request, ?Clients $client = null): array
    {
        return $request->validate([
            'first_name' => ['required', 'string', 'min:5', 'max:30'],
            'last_name' => ['required', 'string', 'min:5', 'max:30'],
            'phone_number' => ['required', 'string', 'max:10'],
            'email' => [
                'required',
                'email',
                Rule::unique('clients', 'email')->ignore($client?->id),
            ],
        ]);
    }
}
